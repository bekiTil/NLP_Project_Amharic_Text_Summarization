import { Component } from '@angular/core';
import { ChatBotService } from './chat-bot.service';
import { ChatFacade } from './chat.facade';
import { Message } from './chat.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  messages: Message[] = [];
  value: string='';
  asked_question: Message = { author: '', text: '' };
  constructor(public chatService: ChatBotService,  public chatFacade: ChatFacade,) { }

  ngOnInit() {
      this.chatFacade.messages$.subscribe((val) => {
      this.messages = this.messages.concat(val);
    });
  }

  sendMessage() {
    this.asked_question = {
      author: "User",
      text: this.value
    };
    this.asked_question.author="User"
    this.asked_question.text=this.value;
this.chatFacade.getResponse(this.asked_question);
    this.value = '';
  }

}
