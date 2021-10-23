import {NgModule} from "@angular/core";
import {MainComponent} from "./main.component";
import {CommonModule} from "@angular/common";

@NgModule({
  declarations: [MainComponent],
  imports: [
    CommonModule
  ],
  exports: [MainComponent]
}) export class MainModule {}
