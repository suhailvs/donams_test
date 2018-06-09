===============================
Jquery post a form and validate
===============================

Frontend
========

`home.html`::

  <h1>Add User</h1><hr />
  <form method="post">{% csrf_token %}
    <div class="form-group">
      <label for="FullName">Full Name</label>
      <input type="text" class="form-control" name="fullname" placeholder="Full Name" id="div_id_fullname">
    </div>
    <div class="form-row">
      <div class="form-group col-md-6">
        <label for="inputEmail4">Email</label>
        <input type="email" class="form-control" placeholder="Email" name="email" id="div_id_email">
      </div>
      <div class="form-group col-md-6">
        <label>Contact Number</label>
        <input class="form-control" placeholder="Contact Number" name="contact" id="div_id_contact">
      </div>
    </div>
    <div class="form-group">
      <label for="inputAddress">Address</label>
      <input type="text" class="form-control" name="address1" placeholder="1234 Main St" id="div_id_address1">
    </div>
    <div class="form-group">
      <label for="inputAddress2">Address 2</label>
      <input type="text" class="form-control" name="address2" placeholder="Apartment, studio, or floor" id="div_id_address2">
    </div>
    <button type="submit" class="btn btn-primary"><span class="fas fa-plus-square"></span> Add User</button>
  </form>

  <script>
  $(document).on( "submit","form", function( event ) {
    event.preventDefault();
    $.post("{% url 'ajax_adduser' %}",$(this).serialize(),function(response) {
      if (response.result == 'success'){
        alert('User details saved successfully.');
        $('#ajaxBox').load(url_showpage+'add');
      }else {
        $("form").find(".errorField").remove();
        for (var key in response.result) {
          error = response.result[key][0];
          field = $("form").find("#div_id_" + key)
          // Attach error message before it
          field.before('<small class="text-danger errorField">'+error+'</small>');
        }
      }
    });
  });
  </script>

Backend
=======

`views.py`::

  import json
  def ajax_adduser(request):
    if request.method=="POST":
      form = UserDetailForm(request.POST)
      if form.is_valid():
        form.save()
        message= 'success'
      else:
        message = dict([(key, value) for key, value in form.errors.items()])
    return HttpResponse(json.dumps({"result": message, }), content_type='application/json')

`forms.py`::
 
  class UserDetailForm(forms.ModelForm):
    def clean_email(self):
      email = self.cleaned_data['email']
      if UserDetail.objects.filter(email=email):
        raise forms.ValidationError("email already exist!")
    return email

    class Meta:
      model = UserDetail
      fields = '__all__'

`urls.py`::

  path('ajx/add/', views.ajax_adduser, name='ajax_adduser'),

