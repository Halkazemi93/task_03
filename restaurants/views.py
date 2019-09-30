from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [{

    		"restaurant_name": "zuma",
    		"food_type": "japanese",
    	},
    	{
    		"restaurant_name": "roberto's",
    		"food_type": "italian",

    	},
    	{
    		"restaurant_name": "eighty-six",
    		"food_type": "burgers",

    	}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {

    		"restaurant_name": "zuma",
    		"food_type": "japanese",
    	}

    }
    return render(request, 'detail.html', context)
