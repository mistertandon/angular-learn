import { HERO_LIST } from './hero-list.constant';
import { ACTIVE, INACTIVE } from './hero.constant';

export class Hero {

  constructor(public name: string, public status: string) { }

  public toggleState(): void {

    this.status = this.status === INACTIVE ? ACTIVE : INACTIVE;
  }
}

export const HERO_INSTANCE = HERO_LIST.map(name => new Hero(name, ACTIVE));