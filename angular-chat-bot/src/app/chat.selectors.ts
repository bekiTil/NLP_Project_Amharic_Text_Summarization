import { Selector } from '@ngxs/store';
import { ChatState, ChatStateModel } from './chat.state';
import { Message } from './chat.model';

export class ChatSelector {
  @Selector([ChatState])
  static messages(stateModel: ChatStateModel): Message[] {
    return stateModel.messages;
  }

  @Selector([ChatState])
  static loading(stateModel: ChatStateModel): boolean {
    return stateModel.loading;
  }

  
}
