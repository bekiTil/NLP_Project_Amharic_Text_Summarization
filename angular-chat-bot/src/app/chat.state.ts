import { Injectable } from '@angular/core';
import { Action, State, StateContext, StateToken } from '@ngxs/store';
import { tap } from 'rxjs';
import { Message } from './chat.model';
import { ChatBotService } from './chat-bot.service';
import { GetMessages, GetResponse } from './chat.actions';

export interface ChatStateModel {
  messages: Message[];
  loading: boolean;
  
}

const CATEGORY_STATE_TOKEN = new StateToken<ChatStateModel>(
  'Chat',
);

@State<ChatStateModel>({
  name: CATEGORY_STATE_TOKEN,
  defaults: {
    messages: [],
    loading:false
  },
})
@Injectable()
export class ChatState {
  constructor(private chatService: ChatBotService) {}

  @Action(GetMessages)
  getMessage(
    { patchState, dispatch }: StateContext<ChatStateModel>,
    {  }: GetMessages,
  ) {

    patchState({loading:true})
    return this.chatService.getMessages().pipe(
      tap((messages: Message[]) => {
       
        patchState({
      messages:messages,
      loading:false
         
        });
       
      }),
    );
  }

  @Action(GetResponse)
  getResponse(
    { patchState, getState, dispatch }: StateContext<ChatStateModel>,
    { filter }: GetResponse,
  ) {
    patchState({loading:true})
   
    return this.chatService.getResponse(filter).pipe(
      tap((messages:Message[]) => {
        patchState({
          messages:messages,
          loading:false
        });
       
      }),
    );
  }
 
}
