from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):
    return Response("passed! ({}) but the logic for this is stillunder development".format(request.user.username))