from django.http import HttpResponse
from django.shortcuts import render
from main import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


@api_view(['GET'])
def list_school(request):
    schools = models.School.objects.all()
    serializer = serializers.SchoolSer(schools, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def crt_schl(request):
    if request.user.is_superuser:
        try:
            models.School.objects.create(
                name = request.data['name'], 
                city = request.data['city'],
                about = request.data['about'],
                address = request.data['address'],
            )
            res = {'status':'Created school'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)


@api_view(['PUT'])
def upd_schl(request, id):
    school = models.School.objects.get(id)
    if request.user.is_superuser or school.school == request.user:
        try:
            school.name = request.data['name'] 
            school.city = request.data['city']
            school.about = request.data['about']
            school.address = request.data['address']
            school.save()
            res = {'status':'Updated school'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def d_schl(request, id):
    school = models.School.objects.get(id)
    if request.user.is_superuser:
        try:
            school.delete()
            res = {'status':'Deleted school'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def list_subject(request):
    subject = models.Subject.objects.all()
    serializer = serializers.SubSer(subject, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def cr_sbjct(request):
    if request.user.is_superuser:
        try:
            models.Subject.objects.create(
                subject_name = request.data['subject_name'],
                school = models.School.objects.get(id=request.data['school_id']),
            )
            res = {'status':'Created Subject'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {"status':'You don't have permission:("}
    return Response(res)


@api_view(['PUT'])
def upd_sbjct(request, id):
    subject = models.Subject.objects.get(id=id)
    if request.user.is_superuser or subject.teacher == request.user:
        try:
            subject.subject_name = request.data['subject_name']
            subject.school = models.School.objects.get(id=request.data['school_id'])
            subject.save()

            res = {'status':'Updated Subject'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {"status':'You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def del_sub(request, id):
    subject = models.Subject.objects.get(id=id)
    if request.user.is_superuser or subject.teacher == request.user:
        try:
            subject.delete()
            res = {'status':'Delated Subject'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)

    
@api_view(['GET'])
def list_users(request):
    users = models.IqroUser.objects.all()
    serializer = serializers.ListUserSer(users, many= True)
    return Response(serializer.data)


# @login_required()
@api_view(['POST'])
def create_user(request):
    if request.user.is_superuser:
        try:
            models.IqroUser.objects.create(
            school = models.School.objects.get(id=request.data['school_id']),
            username = request.data['username'],
            password = request.data['password'],
            email = request.data['email'],
            is_active = True,
            is_staff = True if request.data['is_staff'] == 'True'else False,
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            s_name = request.data['s_name'],#Father name (Otasini ismi)
            phone_num = request.data['phone_number'],
            
            type = request.data['type'],#( 1,"Super"),(2,'admin'),(3,'head teacher'),(4,'teacher')
            birthday = request.data['bithday'],
            passport_ser = request.data['passport_seria'],
            passport_JSHSHR = request.data['jshshr'],
            finger_id = request.data['finger_id'],
            telegram = request.data['telegram'],
            )
            res = {'status':'Created'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)


@api_view(['PUT'])
def upgruser(request, id):
    user = models.IqroUser.objects.get(id=id)
    if request.user.is_superuser or request.user == user:
        try:
            user.school = models.School.objects.get(id=request.data['school_id'])
            user.username = request.data['username']
            user.password = request.data['password']
            user.email = request.data['email']
            user.is_active = True if request.data['is_active'] == "1" else False
            user.is_staff = True if request.data['is_staff'] == '1' else False
            user.first_name = request.data['first_name']    
            user.last_name = request.data['last_name']
            user.s_name = request.data['s_name']#Father name (Otasini ismi)
            user.phone_num = request.data['phone_number']
            
            user.type = request.data['type']#( 1,"Super"),(2,'admin'),(3,'head teacher'),(4,'teacher')
            user.birthday = request.data['bithday']
            user.passport_ser = request.data['passport_seria']
            user.passport_JSHSHR = request.data['jshshr']
            user.finger_id = request.data['finger_id']
            user.telegram = request.data['telegram']
            user.save()
            res = {'status':'Updated'}
        except:
            res = {'status':'Something went wrong'}
    else:
        res = {'status':"You don't have permission:("}
    return Response(res)


@api_view(["GET"])
def del_user(request, id):
    try:
        user = models.IqroUser.objects.get(id=id)
        if request.user.is_superuser:
            user.delete()
            res = {"status": "delated"}
        else:
            res = {"status": "You don't have permission:("}
    except:
            res = {'status':'Something went wrong'}      
    return Response(res)


@api_view(["GET"])
def list_class(request):
    clas = models.Cla_ss.objects.all()
    serializer = serializers.ClasSer(clas, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def crt_clss(request):
    if request.is_superuser:
        try:
            models.Cla_ss.objects.create(
            title = request.data['title'],
            teacher = models.IqroUser.objects.get(id=request.data['teacher']),
            school = models.School.objects.get(id=request.data['school_class'])
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["PUT"])
def upd_clss(request, id):
    clss = models.Cla_ss.objects.get(id=id)
    if request.is_superuser:
        try:
            clss.title = request.data['title']
            clss.teacher = models.IqroUser.objects.get(id=request.data['teacher'])
            clss.school = models.School.objects.get(id=request.data['school_class'])
            clss.save()
            
            res = {"status": "Update"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["GET"])
def del_clss(request, id):
    clss = models.Cla_ss.objects.get(id=id)
    if request.is_superuser:
        try:
            clss.delete()
            res = {"status": "Delete"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def list_par(request):
    parent = models.Parent.objects.all()
    serializer = serializers.ListPerSer(parent, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def crt_parnt(request):
    if request.is_superuser:
        try:
            models.Parent.objects.create(
            who = request.data['who'],
            grf = request.data['grf'], #promis
            phone = request.data['tel_per'],
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["PUT"])
def upd_par(request, id):
    par = models.Parent.objects.get(id=id)
    if request.is_superuser:
        try:
            par.who = request.data['who']
            par.grf = request.data['grf']#promis
            par.phone = request.data['tel_per']
            par.save()
            
            res = {"status": "Update"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["GET"])
def d_par(request, id):
    par = models.Parent.objects.get(id=id)
    if request.is_superuser:
        try:
            par.delete()
            res = {"status": "Delete"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def puplist(request):
    pupil = models.Pupil.objects.all()
    serializer = serializers.ListPupSer(pupil, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def crt_pup(request):
    if request.is_superuser:
        try:
            models.Pupil.objects.create(
                f_name = request.data['f_name'],
                s_name = request.data['s_name'],
                l_name = request.data['l_name'],
                cla_ss = models.Cla_ss.objects.get(id=request.data['cla_ss_id']),
                finger_id = request.data['finger_id'],
                telegram = request.data['telegram'],
                school = models.School.objects.get(id=request.data['school_id']),
                parent = request.data['parent'],
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["PUT"])
def upd_pup(request, id):
    if request.is_superuser:
        try:
            pupl = models.Pupil.objects.get(id=id)
            pupl.f_name = request.data['f_name']
            pupl.s_name = request.data['s_name']
            pupl.l_name = request.data['l_name']
            pupl.cla_ss = models.Cla_ss.objects.get(id=request.data['cla_ss_id'])
            pupl.finger_id = request.data['finger_id']
            pupl.telegram = request.data['telegram']
            pupl.school = models.School.objects.get(id=request.data['school_id'])
            pupl.parent = request.data['parent']
            pupl.save()
            
            res = {"status": "Update"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


def dlt_pup(request, id):
    if request.is_superuser:
        try:
            pupl = models.Pupil.objects.get(id=id)
            pupl.delete()
            
            res = {"status": "Delete"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(['GET'])
def yadlist(request):
    yadfa = models.PayHis.objects.all()
    serializer = serializers.ListPaySer(yadfa, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def ayadfa_tar(request):
    if request.is_superuser:
        try:
            models.PayHis.objects.create(
                parent = models.Parent.objects.get(id=request.data['parent_id']),
                pupil = models.Pupil.objects.get(id=request.data['pupil_id']),
                summa = request.data['summa'],
                paymon = request.data['paymon'],
               
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["PUT"])
def uayadfa_tar(request, id):
    if request.user.is_superuser:
        try:
            pay = models.PayHis.objects.get(id = id)
            pay.parent = models.Parent.objects.get(id=request.data['parent_id'])
            pay.pupil = models.Pupil.objects.get(id=request.data['pupil_id'])
            pay.summa = request.data['summa']
            pay.paymon = request.data['paymon']
            pay.save()
            
            res = {"status": "Update"}
        except models.PayHis.DoesNotExist:
            res = {"status": "Pupil does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)


@api_view(["GET"])
def dayadfa_tar(request, id):
    if request.user.is_superuser:
        try:
            pay = models.PayHis.objects.get(id=id)
            pay.delete()
            
            res = {"status": "Delete"}
        except models.PayHis.DoesNotExist:
            res = {"status": "PayHis does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)



@api_view(['GET'])
def saleLis(request):
    sl = models.SaleHis.objects.all()
    serializer = serializers.SaleHisList(sl, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def salc(request):
    if request.is_superuser:
        try:
            models.SaleHis.objects.create(
                payhis = models.PayHis.objects.get(id= request.data['payhis_id']), 
                salesum = request.data['salesum'],
                aboutsale = request.data['aboutsale'],
                date = request.data['date'],
                status = request.data['status'],
                forwhat = request.data['forwhat'],
               
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["PUT"])
def salhisupd(request, id):
    if request.user.is_superuser:
        try:
            salhis = models.SaleHis.objects.get(id=id), 
            salhis.salesum = request.data['salesum'],
            salhis.aboutsale = request.data['aboutsale'],
            salhis.date = request.data['date'],
            salhis.status = request.data['status'],
            salhis.forwhat = request.data['forwhat'],
               
            
            res = {"status": "Update"}
        except models.SaleHis.DoesNotExist:
            res = {"status": "Pupil does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)


@api_view(["GET"])
def dsalhis(request, id):
    if request.user.is_superuser:
        try:
            pay = models.PayHis.objects.get(id=id)
            pay.delete()
            
            res = {"status": "Delete"}
        except models.PayHis.DoesNotExist:
            res = {"status": "PayHis does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)


@api_view(["GET"])
def liss(request):
    sl = models.SalHis.objects.all()
    serializer = serializers.SalHisList(sl, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def scrt(request):
    if request.is_superuser:
        try:
            models.SalHis.objects.create(
                per = models.IqroUser.objects.get(id=request.data['person_id']),
                sal = request.data['allsal'],
                plast = request.data['plastik'],
                cash = request.data['cash'],
                shtrf = request.data['shtraf'],
                bonus = request.data['bonus'],
                periud = request.data['periud'],
                date = request.data['date'],
            )
            res = {"status": "Create"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)
     

@api_view(["PUT"])
def supd(request, id):
    if request.is_superuser:
        try:
            sal = models.SalHis.objects.get(id=id)
            sal.per = models.IqroUser.objects.get(id=request.data['person_id'])
            sal.sal = request.data['allsal']
            sal.plast = request.data['plastik']
            sal.cash = request.data['cash']
            sal.shtrf = request.data['shtraf']
            sal.bonus = request.data['bonus']
            sal.periud = request.data['periud']
            sal.date = request.data['date']
            sal.save()
            
            res = {"status": "Update"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["GET"])
def sdel(request, id):
    if request.user.is_superuser:
        try:
            pay = models.SalHis.objects.get(id=id)
            pay.delete()
            
            res = {"status": "Deleted"}
        except models.PayHis.DoesNotExist:
            res = {"status": "PayHis does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)



@api_view(["GET"])
def lisq(request):
    sl = models.Chiq.objects.all()
    serializer = serializers.ChiqLsSer(sl, many=True)
    return Response(serializer.data)



@api_view(["POST"])
def chiq_crt(request):
    if request.is_superuser:
        try:
            models.Chiq.objects.create(
                oziqo = request.data['oziqo'], 
                about = request.data['about'],
                tpe = request.data['tpe'],
                per = request.data['per'],
            )
            res = {"status": "Created"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)
     

@api_view(["PUT"])
def chupd(request, id):
    if request.is_superuser:
        try:
            sal = models.Chiq.objects.get(id=id)
            sal.oziqo = request.data['oziqo'], 
            sal.about = request.data['about'],
            sal.tpe = request.data['tpe'],
            sal.per = request.data['per'],
                
            sal.save()
            
            res = {"status": "Updated"}
        except:
                res = {'status':'Something went wrong'}      
    else:
            res = {"status": "You don't have permission:("}
    return Response(res)


@api_view(["GET"])
def chdel(request, id):
    if request.user.is_superuser:
        try:
            pay = models.Chiq.objects.get(id=id)
            pay.delete()
            
            res = {"status": "Deleted"}
        except models.PayHis.DoesNotExist:
            res = {"status": "PayHis does not exist"}
    else:
        res = {"status": "You do not have access"}
    return Response(res)