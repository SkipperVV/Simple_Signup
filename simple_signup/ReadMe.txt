
Регистрация посредством провайдера
В случае регистрации и входа через провайдер необходимо проделать ещё некоторые действия.
Для начала нужно войти в панель администратора и перейти на вкладку Sites:
Далее необходимо перейти на страницу единственного объекта и отредактировать следующим образом:
Domain name: 127.0.0.1
Сохраните изменения.

Далее необходимо настроить API Google для работы с вашим сервисом. Перейдите на страницу разработчиков.
Вам будет предложено создать проект. 
Сделал. Ссылка:
https://console.cloud.google.com/apis/dashboard?pli=1&project=myproject-399913&supportedpurview=project

После чего вам необходимо получить Client ID.
Для этого перейдите по следующей ссылке: <+Enable APIS and Services>
Подключите следующее API: IAM Service Account Credentials API (найти поисковиком)
Enable
Credentials (Реквизиты для входа)
Create OAuth client ID
Client ID: 564458227682-tp5a4ooq35lnssoh6rmrrk0r9qr2sgch.apps.googleusercontent.com
Client secret: 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
(Моя Страница credentials: https://console.cloud.google.com/apis/credentials?project=myproject-399913
<+Create Credentials>)

Вы увидите окно с идентификатором клиента и секретным ключом. Не закрывайте это окно.
Откройте панель администратора на странице: 
http://127.0.0.1:8000/admin/socialaccount/socialapp/ 
и создайте новое приложение Social applications.

Название, как и провайдер, можно вписать Google. В поля Client ID и Secret Key введите полученные 
на консоли разработчиков строки с идентификатором и ключом и сохраните изменения на панели администратора.

После чего проверьте работоспособность путём попытки авторизации через Google на 
странице авторизации вашего свежесозданного сайта. Если все действия выполнены верно, 
вам должно быть предложено завершить регистрацию.
------------
Ссылка на созданный сайт Google 
https://console.cloud.google.com/apis/credentials?project=myproject-399913

--------Добавление в группы при регистрации-----------------------------------------------------------------

Добавим следующий код в файл, например, sign/models.py. В идеале, конечно, скрипты, относящиеся к формам, нужно хранить в отдельном файле forms.py, но для нас сейчас это не является принципиальным.
<
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class BasicSignupForm(SignupForm):
    
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user
>
Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию, необходимо 
добавить строчку в файл настроек проекта settings.py:

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}