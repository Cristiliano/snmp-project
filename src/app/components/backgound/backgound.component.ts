import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-backgound',
  templateUrl: './backgound.component.html',
  styleUrls: ['./backgound.component.scss'],
})
export class BackgoundComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {
    let video = document.getElementById('bgvid') as HTMLVideoElement;
    video.defaultPlaybackRate = 1;
  }
}
