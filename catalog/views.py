from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import File, Book, Loan, Student
from .serializer import FileSerializer, LoanSerializer, UserSerializer

from datetime import datetime, timedelta
from fuzzywuzzy import process


class FileList(APIView):
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)


class BookFiles(APIView):
    def getObjects(self, book):
        try:
            return File.objects.all().filter(book=book)
        except:
            raise Http404

    def get(self, request, book, format=None):
        file = self.getObjects(book)
        serializer = FileSerializer(file, many=True)
        data = {
            'book': book,
            'files': [f['file'] for f in serializer.data]
        }
        return Response(data)


class BookLoans(APIView):
    permission_classes = (IsAuthenticated,)
    def getLoans(self, book):
        try:
            bookID = Book.objects.get(id=book).id
            return Loan.objects.all().filter(book=bookID)
        except:
            raise Http404

    def get(self, request, book, format=None):
        loan = self.getLoans(book)
        serializer = LoanSerializer(loan, many=True)
        return Response(serializer.data)


class LoanAdd(APIView):
    permission_classes = (IsAuthenticated,)
    def getLoans(self, book):
        try:
            return Loan.objects.all().filter(book=book)
        except:
            raise Http404

    def getRanges(self, l):
        l = sorted(l)
        pairs = zip(l[:-1], l[1:])
        c = [0,]

        for n, (a, b) in enumerate(pairs):
            if (b - a).days > 1:
                c.append(n)
                c.append(n + 1)

        c.append(len(l) - 1)

        pairs = zip(c[::2], c[1::2])
        return [(l[a], l[b]) if a != b else l[a] for a, b in pairs]


    def post(self, request):
        data = request.data
        user = UserSerializer(request.user).data
        student = Student.objects.get(user=user['id'])
        loans = self.getLoans(data['book'])

        dates = set()
        for l in loans:
            dates |= {l.loanStart + timedelta(d) for d in range(l.loanDuration + 1)}

        start = datetime.strptime(data['loanStart'], '%Y-%m-%d').date()
        end = start + timedelta(int(data['loanDuration']))

        newLoan = {start + timedelta(d) for d in range((end - start).days + 1)}
        intersections = list(dates & newLoan)

        data['student'] = student.id
        serializer = LoanSerializer(data=data)

        if serializer.is_valid():
            if intersections:
                return Response(
                    {
                        'error': 'Пересечение периодов бронирования',
                        'interseptions' : self.getRanges(intersections)
                    },
                    status.HTTP_409_CONFLICT
                )
            else:
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(user, status.HTTP_409_CONFLICT)


class BookSearch(APIView):
    permission_classes = (IsAuthenticated,)
    def search(self, data):
        books = Book.objects.all()
        resID = set([b.id for b in books])

        for key in ['title', 'isbn']:
            if key in data:
                values = [b.__dict__[key] for b in books]
                fuzzy = process.extractBests(data[key], values, score_cutoff=60)
                fvalues = [val for val, _ in fuzzy]
                ids = [b.id for b in books if b.__dict__[key] in fvalues]
                resID &= set(ids)

        if 'author' in data:
            values = [b.author.lname for b in books]
            fuzzy = process.extractBests(data['author'], values, score_cutoff=60)
            fvalues = [val for val, _ in fuzzy]
            ids = [b.id for b in books if b.author.lname in fvalues]
            resID &= set(ids)

        resBooks = [{
            'id': b.id,
            'title': b.title,
            'author': f'{b.author.fname} {b.author.lname}',
            'isbn': b.isbn
        } for b in books if b.id in resID]

        return resBooks

    def get(self, request):
        resBooks = self.search(request.data)

        if resBooks != set():
            return Response(resBooks, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)