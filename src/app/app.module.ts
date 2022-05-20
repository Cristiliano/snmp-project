import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { BackgoundComponent } from './components/backgound/backgound.component';
import { InputContainerComponent } from './components/input-container/input-container.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BlockGroupComponent } from './components/block-group/block-group.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BackgoundComponent,
    InputContainerComponent,
    BlockGroupComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
