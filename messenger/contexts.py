def count_unread_mail(request):
    if request.user.is_anonymous():
        return {'unread_mail': 0}    
    else:
        unread = request.user.messages_received.filter(read=False)
        return {'unread_mail': len(unread)}