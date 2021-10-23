import {NgModule} from "@angular/core";
import {SchedulePlanComponent} from "./shedule-plan.component";
import {SchedulePlanService} from "./schedule-plan.service";

@NgModule({
  declarations: [SchedulePlanComponent],
  providers: [SchedulePlanService],
  exports: [SchedulePlanComponent]
}) export class SchedulePlanModule {}
