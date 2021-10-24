import {NgModule} from "@angular/core";
import {MainComponent} from "./main.component";
import {CommonModule} from "@angular/common";
import {AgGridModule} from "ag-grid-angular";

@NgModule({
  declarations: [MainComponent],
    imports: [
        CommonModule,
        AgGridModule
    ],
  exports: [MainComponent]
}) export class MainModule {}
