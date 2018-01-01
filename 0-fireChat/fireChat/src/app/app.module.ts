import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { AngularFireDatabase, FirebaseObjectObservable } from 'angularfire2/database-deprecated';
import { AngularFireAuthModule } from 'angularfire2/auth';

import { AppComponent } from './app.component';
import { ChatFormComponent } from './chat-form/chat-form.component';
import { ChatroomComponent } from './chatroom/chatroom.component';
import { FeedComponent } from './feed/feed.component';
import { MessageComponent } from './message/message.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { SignupFormComponent } from './signup-form/signup-form.component';
import { NavbarComponent } from './navbar/navbar.component';
import { UserListComponent } from './user-list/user-list.component';
import { UserItemComponent } from './user-item/user-item.component';

import { ChatService } from './services/chat.service';
import { AuthService } from './services/auth.service';

import { appRoutes } from '../routes';
import { environment } from '../environments/environment';

import {MaterialModule } from './material.module';

@NgModule({
  declarations: [
    AppComponent,
    ChatFormComponent,
    ChatroomComponent,
    FeedComponent,
    MessageComponent,
    LoginFormComponent,
    SignupFormComponent,
    NavbarComponent,
    UserListComponent,
    UserItemComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    AngularFireModule,
    AngularFireDatabaseModule,
    AngularFireAuthModule,
    AngularFireModule.initializeApp(environment.firebase),
  ],
  providers: [AuthService, ChatService, AngularFireDatabase],
  bootstrap: [AppComponent]
})
export class AppModule { }
