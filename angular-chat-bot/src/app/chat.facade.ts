import { Injectable } from '@angular/core';
import { Actions, ofActionSuccessful, Select, Store } from '@ngxs/store';
import { Observable } from 'rxjs';
import { Message } from './chat.model';
import { ChatSelector } from './chat.selectors';
import { GetMessages, GetResponse } from './chat.actions';

@Injectable({
  providedIn: 'root',
})
export class ChatFacade {
  @Select(ChatSelector.messages)
  messages$!: Observable<Message[]>;

  @Select(ChatSelector.loading)
  loading$!: Observable<boolean>;

  constructor(
    private store: Store,
    private actions$: Actions,
  ) {}




  getMessages() {
    return this.store.dispatch(new GetMessages());
  }

  getResponse(message:Message) {
    return this.store.dispatch(new GetResponse(message));
  }
 
}
