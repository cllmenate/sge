from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from django.urls import reverse_lazy
from outflows import models, forms


# Create your views here.
class OutflowListView(ListView):
    model = models.Outflows
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = (self.request.GET.get('product') or '').strip()
        serial_number = (self.request.GET.get('serial_number') or '').strip()
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        if serial_number:
            queryset = queryset.filter(
                product__serial_number__icontains=serial_number
            )
        if category:
            queryset = queryset.filter(product__category__id=category)
        if brand:
            queryset = queryset.filter(product__brand__id=brand)

        return queryset


class OutflowCreateView(CreateView):
    model = models.Outflows
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = models.Outflows
    template_name = 'outflow_detail.html'
