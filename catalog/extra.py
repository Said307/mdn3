



 


class Orders():

    def __init__(self,request):
        self.session =request.session
        self.myorders = self.session.get('orders')
        if not self.myorders:
            self.myorders=self.session['orders'] = {}

    
    def add_order(self,**kwargs):
        for a,b in kwargs.items():
            self.myorders[a]=b
        self.session.modified=True

    
    def print_order(self):

        return self.myorders






