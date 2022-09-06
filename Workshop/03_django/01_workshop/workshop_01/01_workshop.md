# 01 workshop

1. intro/urls.py
    
    ```python
    ...생략...
    from articles import views
    
    urlpatterns = [
    	...생략...
    	path('dinner/<int:people>/<str:menu>', views.dinner),
    ]
    ```
    
2. pages/views.py
    
    ```python
    def dinner(request, people, menu):
        context = {
            'people' : people,
            'menu' : menu,
            }
        return render(request, 'dinner.html', context)
    ```
    
3. templates/dinner.html
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <h1>저녁메뉴</h1>
      <h1>저녁 먹을 사람?! {{people}}</h1>
      <h1>어떤 메뉴?! {{menu}}</h1>
    </body>
    </html>
    ```