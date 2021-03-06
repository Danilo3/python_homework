from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, BookingRoomForm

# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login, authenticate

# Create your views here.
from django.views import generic


from hotel.models import Room, Profile, Booking

from django.contrib.auth.decorators import login_required


class IndexView(generic.TemplateView):
    template_name = 'hotel/index.html'


class RoomsView(generic.ListView):
    template_name = 'hotel/rooms.html'
    context_object_name = 'all_rooms_list'

    def get_queryset(self):
        return Room.objects.all()


class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'hotel/room.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RoomDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['booking_form'] = BookingRoomForm()
        return context




def contactsView(request):
    return render(request, 'hotel/contacts.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "hotel/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)




class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "hotel/registration/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'hotel/registration/login.html', {'form': form})


@login_required
def dashboard(request):
    photo = request.user.profile.photo
    profile = Profile.objects.get(user = request.user)
    reservations = profile.reservations
    return render(request, 'hotel/dashboard.html', {'section': 'dashboard', "photo": photo, "reservations":reservations})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request, 'hotel/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'hotel/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'hotel/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


@login_required
def booking(request):
    if request.method =='POST':
        booking_form = BookingRoomForm(request.POST)
        if booking_form.is_valid():
            new_booking = booking_form.save(commit=False)
            new_booking.room =Room.objects.get(id = request.POST['room_id'])
            new_booking.save()
            profile = request.user.profile
            profile.reservations.add(new_booking)
            profile.save()
        return render(request, 'hotel/dashboard.html')