from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404

from django_filters.views import FilterView
from djpjax import PJAXResponseMixin

from .models import BoardPost
from .filters import BoardPostFilter


class BoardListView(PJAXResponseMixin, FilterView):
    template_name = 'boards/list.html'
    pjax_template_name = "boards/includes/pjax_list.html"
    model = BoardPost
    filterset_class = BoardPostFilter

    def get_queryset(self):
        queryset = super(BoardListView, self).get_queryset()
        queryset = queryset.filter(enabled=True).select_related('user')
        return queryset


class BoardCreateView(CreateView):
    model = BoardPost
    template_name = 'boards/form.html'
    fields = ['title', 'text', 'category', 'tags']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BoardCreateView, self).form_valid(form)


class BoardUpdateView(UpdateView):
    model = BoardPost
    template_name = 'boards/form.html'
    fields = ['title', 'text', 'category', 'tags']

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        response = super(BoardUpdateView, self).get(request, *args, **kwargs)
        if request.user != self.object.user:
            raise Http404
        return response

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        response = super(BoardUpdateView, self).post(request, *args, **kwargs)
        if request.user != self.object.user:
            raise Http404
        return response
