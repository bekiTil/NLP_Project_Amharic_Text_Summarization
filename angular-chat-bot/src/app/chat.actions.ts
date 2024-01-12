import { Message } from "./chat.model";

export class GetMessages {
    static readonly type = `[Message] ${GetMessages.name}`;
    constructor() {}
  }
  
  export class GetResponse {
    static readonly type = `[Indicator] ${GetResponse.name}`;
    constructor(public filter: Message) {}
  }