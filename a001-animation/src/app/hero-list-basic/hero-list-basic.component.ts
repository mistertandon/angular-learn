import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { trigger, state, style, transition, animate } from '@angular/animations'

import { ACTIVE, INACTIVE } from './../services/hero.constant'
import { Hero } from './../services/hero.class'
import { HeroService } from './../services/hero.service';

@Component({
  selector: 'app-hero-list-basic',
  templateUrl: './hero-list-basic.component.html',
  styleUrls: ['./hero-list-basic.component.css'],
  animations:
    [
      trigger(
        'herostatus',
        [
          state(ACTIVE, style(
            {
              backgroundColor: '#79FF4D'
            })
          ),
          state(INACTIVE, style(
            {
              backgroundColor: '#FF94A9'
            })
          ),
          transition(`${ACTIVE} => ${INACTIVE}`, animate('100ms easy-in')),
          transition(`${INACTIVE} => ${ACTIVE}`, animate('100ms easy-out'))
        ]
      )
    ],
  encapsulation: ViewEncapsulation.None
})
export class HeroListBasicComponent implements OnInit {

  @Input()
  public heros: Hero[];

  constructor(private HeroService_Ref: HeroService) { }

  ngOnInit() {

    console.log(this.heros);
  }


}
