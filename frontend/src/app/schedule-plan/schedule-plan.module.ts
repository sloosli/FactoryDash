import {NgModule} from "@angular/core";
import {SchedulePlanComponent} from "./shedule-plan.component";
import {SchedulePlanService} from "./schedule-plan.service";
import {CommonModule} from "@angular/common";
import {AgGridModule} from "ag-grid-angular";

@NgModule({
    declarations: [SchedulePlanComponent],
    providers: [SchedulePlanService],
  imports: [
    CommonModule,
    AgGridModule
  ],
    exports: [SchedulePlanComponent]
}) export class SchedulePlanModule {}
