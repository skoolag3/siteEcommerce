from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('pagamento/', views.list_pagamento, name='list_pagamento'),
    path('pagamento/inserir/', views.ins_pagamento, name='ins_pagamento'),
    path('pagamento/atualizar/<int:pk>', views.upd_pagamento, name='upd_pagamento'),
    path('pagamento/deletar/<int:pk>', views.del_pagamento, name='del_pagamento'),
]
    