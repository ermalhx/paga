from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def prova(request):
    pb = 0
    pn = 0
    sp = 0
    sm = 0
    shp = 0
    shm = 0
    tap = 0
    pagaminimale = 34000
    pagamax = 149954
    try:
        if request.method == 'POST':
            pb = request.POST.get('pbruto')
            pb = float(pb)
            if pb<0:
                messages.info(request,"Paga bruto nuk mund te jete me e vogel se 0")
            elif pb <= 34000 and pb<=0:
                sp = pagaminimale * 0.15
                sm = pagaminimale * 0.095
                shp = pagaminimale * 0.017
                shm = pagaminimale *0.017
                pn = pb - sm - shm
            elif pb <= 40000 and pb >= pagaminimale:
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                pn = pb - sm - shm
            elif pb > 40000 and pb <= 50000:
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.065
                pn = pb - sm - shm - tap
            elif pb > 50000 and pb <= 149954:
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.13
                pn = pb - sm - shm - tap
            elif pb > 149954 and pb <= 200000:
                sp = pagamax * 0.15
                sm = pagamax * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.13
                pn = pb - sm - shm - tap
            elif pb > 200000:
                sp = pagamax * 0.15
                sm = pagamax * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-200000) * 0.23 + 22100
                pn = pb - sm - shm - tap
        context = {
            'pb':pb,
            'sp':sp,
            'sm':sm,
            'shp':shp,
            'shm':shm,
            'tap':tap,
            'pn':pn,
        }
    except:
        context ={
        
    }
    return render(request,'pagat.html',context)
def paganeto(request):
    pb = 0
    pn = 0
    sp = 0
    sm = 0
    shp = 0
    shm = 0
    tap = 0
    pagaminimale = 34000
    pagamax = 149954
    try:
        if request.method == 'POST':
            pn = request.POST.get('pneto')
            pn = float(pn)
            if pn<0:
                messages.info(request,"Paga neto nuk mund te jete me e vogel se 0")
            elif pn is None:
                pb = 0
                sp = 0
                sm = 0
                shp = 0
                shm = 0
            elif pn <=30192:
                pb = pn + (pagaminimale *0.095) + (pagaminimale*0.017)
                sp = pagaminimale * 0.15
                sm = pagaminimale * 0.095
                shp = pagaminimale * 0.017
                shm = pagaminimale *0.017
            elif pn <= 35520 and pn >30192:
                pb = pn / (1-0.095-0.017)
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
            elif pn > 35520 and pn <= 43100:
                pb = (pn - (30000*0.065))/(1-0.095-0.017-0.065)
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.065
            elif pn > 43100 and pn <= 117565.1:
                pb = (pn - (30000*0.13))/(1-0.095-0.017-0.13)
                sp = pb * 0.15
                sm = pb * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.13
            elif pn > 117565.1 and pn <= 160254.4:
                pb = (pn +(pagamax*0.095) - (30000*0.13))/(1-0.13-0.017)
                sp = pagamax * 0.15
                sm = pagamax * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-30000) * 0.13
            elif pn > 160254.4:
                pb = (pn+(pagamax*0.095)+22100-(200000*0.23))/(1-0.23-0.017)
                sp = pagamax * 0.15
                sm = pagamax * 0.095
                shp = pb * 0.017
                shm = pb *0.017
                tap = (pb-200000) * 0.23 + 22100
        context = {
            'pb':pb,
            'pn':pn,
            'sp':sp,
            'sm':sm,
            'shp':shp,
            'shm':shm,
            'tap':tap,
            'pn':pn,
        }
    except:
        context ={
        
    }
    return render(request,'pneto.html',context)
