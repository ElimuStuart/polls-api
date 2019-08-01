from rest_framework import generics

from .models import Poll, Choice
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer

class PollList(generics.ListAPIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)


class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)