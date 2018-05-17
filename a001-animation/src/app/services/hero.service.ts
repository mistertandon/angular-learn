import { Injectable } from '@angular/core';

import { Hero, HERO_INSTANCE } from './hero.class'
import { HERO_LIST } from './hero-list.constant'
import { INACTIVE, ACTIVE } from './hero.constant'

@Injectable()
export class HeroService {

  private heros: Hero[] = [];

  public getHeros(): Hero[] {

    return this.heros;
  }

  public canAddHero(): boolean {

    return HERO_INSTANCE.length > this.heros.length;
  }

  public addActiveHero(): void {

    let hero: Hero = HERO_INSTANCE[this.heros.length];
    hero.status = ACTIVE;

    this.heros.push(hero);
  }

  public addInactiveHero(): void {

    let hero: Hero = HERO_INSTANCE[this.heros.length];
    hero.status = INACTIVE;

    this.heros.push(hero);
  }

  public canRemoveHero(): boolean {

    return this.heros.length > 0;
  }

  public deleteHero(): void {

    this.heros.length -= 1;
  }


}
