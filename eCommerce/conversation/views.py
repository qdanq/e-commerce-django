from django.shortcuts import render, get_object_or_404, redirect
from item.models import Product
from .models import Conversation
from .forms import ConversationMessageForm

def new_conversation(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if product.created_by == request.user:
        return redirect('/')

    conversations = Conversation.objects.filter(product=product).filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.members.add(request.user)
            conversation.members.add(product.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('item:detail', pk=product_pk)
    else:
        form = ConversationMessageForm()
    return render(request, 'new.html', {
        'form': form
        })   
         
