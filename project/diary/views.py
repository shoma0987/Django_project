from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

# Create your views here.
def index(request):
    context = {
        "day_list": Day.objects.all(),
    }
    return render(request, "diary/day_list.html", context)

def add(request):
    #送信内容を基にフォームを作る、POSTじゃなければ空のフォーム
    form = DayCreateForm(request.POST or None)

    # method = POST、つまり送信ボタンを押下時、入力内容が問題なければ
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("diary:index")

    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context={
        "form": form
    }
    return render(request, "diary/day_form.html", context)

def update(reqest, pk):
    #urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk = pk)

    #フォームに取得したDayを紐付ける
    form = DayCreateForm(reqest.POST or None, instance=day)

    #method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if reqest.method == 'POST' and form.is_valid():
        form.save()
        return redirect("diary:index")
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        "form": form
    }
    return render(reqest, "diary/day_form.html", context)

def delete(reqest, pk):
    #urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk = pk)


    #method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if reqest.method == 'POST' :
        day.delete()
        return redirect("diary:index")
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        "day": day,
    }
    return render(reqest, "diary/day_confirm_delete.html", context)

def detail(reqest, pk):
    #urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk = pk)

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        "day": day,
    }
    return render(reqest, "diary/day_detail.html", context)