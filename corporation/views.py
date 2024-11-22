from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import CorporationForm
from .models import Corporation


class NewCorporationView(UserPassesTestMixin, generic.CreateView):
    model = Corporation
    form_class = CorporationForm
    template_name = "corporation/new.html"
    
    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.

        This method uses "reverse_lazy" instead of "reverse" to defer the
        URL resolution until after the object has been created and has a
        primary key (`pk`).

        Returns:
            str: The URL to the detail view of the created post.
        """
        return reverse_lazy("corporation:detail", args=[self.object.pk])

    def form_valid(self, form):
        """
        Process a valid form submission.

        This method overrides the default `form_valid` behavior to automatically
        set the `user` field of the form instance to the currently logged-in user.
        This ensures that any submitted form data is associated with the user who
        is submitting it.

        Parameters:
        form (ModelForm): The form instance containing the data to be validated 
                          and saved.

        Returns:
        HttpResponseRedirect: A redirect to the success URL after the form is 
                              successfully saved.
                            
        Notes:
        - This method assumes that the form's associated model has a `user` field.
        - Superusers are expected to use the Django admin panel for that functionality.
        """
        if self.request.user:
            form.instance.user = self.request.user
            messages.success(
                self.request, "Your corporation has been successfully registered!"
            )
            return super().form_valid(form)
    
        
    def test_func(self):
        """
        Determine if the current user is authenticated.

        This method checks whether the user making the request is logged in. It
        is  commonly used in views that require authentication, allowing only
        authenticated users to access the view's functionality.

        Returns:
        bool: True if the user is authenticated, False otherwise.

        Notes:
        - This method assumes that `self.request.user` is available, which it is in 
          Django's class-based views.
        - Often used in conjunction with Django's `UserPassesTestMixin` to restrict 
          access to authenticated users.
        """
        return self.request.user.is_authenticated


class CorporationDetailView(generic.DetailView):
    model = Corporation
    template_name = "corporation/detail.html"


class EditCorporationView(UserPassesTestMixin, generic.UpdateView):
    model = Corporation
    form_class = CorporationForm
    template_name = "corporation/edit.html"
    
    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful form submission.

        This method overrides the default success URL behavior to redirect
        the user to the detailed view of the updated Corporation instance.

        Returns:
            str: The URL for the corporation detail page, based on the primary
            key of the updated Corporation instance.
        """
        return reverse_lazy("corporation:detail", args=[self.object.pk])
    
    def form_valid(self, form):
        messages.success(
            self.request, "Your corporation details have been successfully updated!"
        )
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_authenticated


class DeleteCorporationView(UserPassesTestMixin, generic.DeleteView):
    model = Corporation
    template_name = "corporation/delete.html"
    
    def get_success_url(self):
        return reverse_lazy("home")
    
    def form_valid(self, form):
        messages.success(
            self.request, "Your corporation has been successfully deleted!"
        )
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_authenticated
