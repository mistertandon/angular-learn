import { Component, OnInit } from '@angular/core';

import { Hero } from './services/hero.class'
import { HeroService } from './services/hero.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  public heros: Hero[];

  constructor(private HeroService_Ref: HeroService) { }

  ngOnInit() {

    this.heros = this.HeroService_Ref.getHeros();
  }

  public canAddHero(): boolean {

    let canAdd: boolean;
    canAdd = this.HeroService_Ref.canAddHero();

    return canAdd;
  }

  public addActiveHero(): void {

    let canAdd: boolean;
    canAdd = this.canAddHero();

    if (canAdd) {

      this.HeroService_Ref.addActiveHero();
    }
  }

  public addInactiveHero(): void {

    let canAdd: boolean;
    canAdd = this.canAddHero();

    if (canAdd) {

      this.HeroService_Ref.addInactiveHero();
    }
  }

  public canRemoveHero(): boolean {

    let canRemove: boolean;
    canRemove = this.HeroService_Ref.canRemoveHero();

    return canRemove;
  }

  public removeHero(): void {

    let canRemove: boolean;
    canRemove = this.canRemoveHero();

    if (canRemove) {

      this.HeroService_Ref.deleteHero();
    }
  }
}