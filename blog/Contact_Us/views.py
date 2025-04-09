from django.shortcuts import redirect, render

from .forms import CustomerFormClass 

def Contant(request):
    # ✅ **Form İşleme**
    if request.method == 'POST':
        form = CustomerFormClass(request.POST)
        if form.is_valid():
            # Formu kaydediyoruz
            form.save()

            # Başarıyla form gönderildikten sonra 'thx.html' sayfasına yönlendirme
            return redirect('thx')  # 'thx' URL ismini doğru ayarladığınızdan emin olun
        else:
            # Geçersiz form gönderimi için hata mesajı
            warning_message = "⚠️ Invalid form submission."
            return render(request, 'home.html', {
                'form': form,
                'warning_message': warning_message
            })

    # Eğer form GET isteğiyle açılıyorsa, boş bir form gösteriyoruz
    else:
        form = CustomerFormClass()

    return render(request, 'contant_us.html', {
        'form': form
    })
def thx(request):
    return render(request, 'thx.html')
# Create your views here.
