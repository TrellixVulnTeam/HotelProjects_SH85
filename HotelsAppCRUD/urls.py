from django.conf.urls import url

from HotelsAppCRUD import views

app_name = "HotelsAppCRUD"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Customer/$', views.Customers, name='customer_index'),
    url(r'^Customer/create/$', views.CustomerCreate.as_view(), name='customer_create'),
    url(r'^Customer/list/$', views.CustomerList.as_view(), name='customer_list'),
    url(r'^Customer/update/(?P<pk>\d+)/$', views.CustomerUpdate.as_view(), name='customer_update'),
    url(r'^Customer/detail/(?P<pk>\d+)/$', views.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^Customer/delete/(?P<pk>\d+)/$', views.CustomerDelete.as_view(), name='customer_delete'),
    url(r'^Hotel/$', views.Hotels, name='hotel_index'),
    url(r'^Hotel/create/$', views.HotelCreate.as_view(), name='hotel_create'),
    url(r'^Hotel/list/$', views.HotelList.as_view(), name='hotel_list'),
    url(r'^Hotel/update/(?P<pk>\d+)/$', views.HotelUpdate.as_view(), name='hotel_update'),
    url(r'^Hotel/detail/(?P<pk>\d+)/$', views.HotelDetail.as_view(), name='hotel_detail'),
    url(r'^Hotel/delete/(?P<pk>\d+)/$', views.HotelDelete.as_view(), name='hotel_delete'),
    url(r'^Room/$', views.Rooms, name='room_index'),
    url(r'^Room/create/$', views.RoomCreate.as_view(), name='room_create'),
    url(r'^Room/list/$', views.RoomList.as_view(), name='room_list'),
    url(r'^Room/update/(?P<pk>\d+)/$', views.RoomUpdate.as_view(), name='room_update'),
    url(r'^Room/detail/(?P<pk>\d+)/$', views.RoomDetail.as_view(), name='room_detail'),
    url(r'^Room/delete/(?P<pk>\d+)/$', views.RoomDelete.as_view(), name='room_delete'),
    url(r'^Billing/$', views.RoomsBilling, name='rooms_billing_index'),
    url(r'^Billing/create/$', views.RoomBillingCreate.as_view(), name='room_billing_create'),
    url(r'^Billing/list/$', views.RoomBillingList.as_view(), name='room_billing_list'),
    url(r'^Billing/update/(?P<pk>\d+)/$', views.RoomBillingUpdate.as_view(), name='room_billing_update'),
    url(r'^Billing/detail/(?P<pk>\d+)/$', views.RoomBillingDetail.as_view(), name='room_billing_detail'),
    url(r'^Billing/delete/(?P<pk>\d+)/$', views.RoomBillingDelete.as_view(), name='room_billing_delete'),
    url(r'^Charge/$', views.RoomsCharge, name='rooms_charge_index'),
    url(r'^Charge/create/$', views.RoomChargesCreate.as_view(), name='rooms_charge_create'),
    url(r'^Charge/list/$', views.RoomChargesList.as_view(), name='rooms_charge_list'),
    url(r'^Charge/update/(?P<pk>\d+)/$', views.RoomChargesUpdate.as_view(), name='rooms_charge_update'),
    url(r'^Charge/detail/(?P<pk>\d+)/$', views.RoomChargesDetail.as_view(), name='rooms_charge_detail'),
    url(r'^Charge/delete/(?P<pk>\d+)/$', views.RoomChargesDelete.as_view(), name='rooms_charge_delete'),
    url(r'^Reservation/$', views.RoomsReservation, name='rooms_reservation_index'),
    url(r'^Reservation/public/$', views.RoomsReservationPub, name='rooms_reservation_public_index'),
    url(r'^Reservation/create/$', views.RoomReservationCreate.as_view(), name='rooms_reservation_create'),
    url(r'^Reservation/public/create/$', views.RoomReservationPubCreate.as_view(), name='rooms_reservation_public_create'),
    url(r'^Reservation/list/$', views.RoomReservationList.as_view(), name='rooms_reservation_list'),
    url(r'^Reservation/public/list/$', views.RoomReservationPubList.as_view(), name='rooms_reservation_public_list'),
    url(r'^Reservation/update/(?P<pk>\d+)/$', views.RoomReservationUpdate.as_view(), name='rooms_reservation_update'),
    url(r'^Reservation/public/update/(?P<pk>\d+)/$', views.RoomReservationPubUpdate.as_view(), name='rooms_reservation_public_update'),
    url(r'^Reservation/detail/(?P<pk>\d+)/$', views.RoomReservationDetail.as_view(), name='rooms_reservation_detail'),
    url(r'^Reservation/public/detail/(?P<pk>\d+)/$', views.RoomReservationPubDetail.as_view(), name='rooms_reservation_public_detail'),
    url(r'^Reservation/delete/(?P<pk>\d+)/$', views.RoomReservationDelete.as_view(), name='rooms_reservation_delete'),
    url(r'^Reservation/lookup/list/$', views.RoomReservationLookupList.as_view(), name='rooms_reservation_lookup_list'),
    url(r'^Reservation/lookup/view/(?P<pk>\d+)/$', views.RoomReservationLookupView.as_view(), name='rooms_reservation_lookup_view'),
    url(r'^Service/$', views.RoomsService, name='rooms_service_index'),
    url(r'^Service/create/$', views.RoomServiceCreate.as_view(), name='rooms_service_create'),
    url(r'^Service/list/$', views.RoomServiceList.as_view(), name='rooms_service_list'),
    url(r'^Service/update/(?P<pk>\d+)/$', views.RoomServiceUpdate.as_view(), name='rooms_service_update'),
    url(r'^Service/detail/(?P<pk>\d+)/$', views.RoomServiceDetail.as_view(), name='rooms_service_detail'),
    url(r'^Service/delete/(?P<pk>\d+)/$', views.RoomServiceDelete.as_view(), name='rooms_service_delete'),
]

