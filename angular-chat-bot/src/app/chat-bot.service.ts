import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { Message } from './chat.model';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})

export class ChatBotService {

  baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getResponse(message: Message) {
    console.log(message)
    return this.http.post<Message[]>(`${this.baseUrl}/items`, {
      author:message.author,
      text:message.text
    });
  }

  getMessages(): Observable<Message[]> {
    return this.http.get<Message[]>(`${this.baseUrl}`)
  }
 
  messageMap = {
    Hi: "Hello",
    "Who are you": "My name is Agular Bot",
    "What is Angular": "Angular is the best framework ever",
    default: "I can't understand. Can you please repeat"
  };

 
}
