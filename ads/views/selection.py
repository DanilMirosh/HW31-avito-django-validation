from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ads.models.selection import Selection
from ads.permission.selection import IsCreatedBy
from ads.serializers.selection import SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer


class SelectionListView(ListAPIView):
    """Display all selections"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    """Display selection by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    """Create new selection"""
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Update add by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]


class SelectionDeleteView(DestroyAPIView):
    """Delete selection by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]
