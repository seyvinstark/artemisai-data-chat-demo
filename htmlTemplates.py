css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''
custom_css = """
<style>
    .input-position {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        z-index: 999;
    }
</style>
"""
# Update the CSS for the text input to be at the center bottom of the page
updated_custom_css = """
<style>
    .input-position {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        z-index: 999;
    }
</style>
"""

# Display the updated CSS


bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
