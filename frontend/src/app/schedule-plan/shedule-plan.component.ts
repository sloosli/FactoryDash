import {Component, OnInit} from "@angular/core";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import {SchedulePlanService} from "./schedule-plan.service";
import {take} from "rxjs/operators";

@Component({
  selector: 'schedule-plan',
  templateUrl: 'schedule-plan.component.html',
  styleUrls: ['schedule-plan.component.scss']
}) export class SchedulePlanComponent implements OnInit{

  constructor(private readonly schedulePlaneService: SchedulePlanService) {}

  public ngOnInit(): void {
    this.schedulePlaneService.getSpeedCheck().pipe(take(1)).subscribe((props: any) => {
      let id: string = '';
      for (let chart of props.kpi_indexes) {
        switch (chart.name){
          case 'Плановый OTIF':
            id = 'otif';
            break;
          case 'Нарушение уровней запасов':
            id = 'level';
            break;
          case 'Загрузка кампаний':
            id = 'load';
            break;
          case 'Обязательный горячий посад, %':
            id = 'posad';
            break;
        }
        this.createSpeedCheck(id, chart);
      }
    });

  }

  private createSpeedCheck(id: string, props: any): void {
    am4core.useTheme(am4themes_animated);

    let chartMin = 0;
    let chartMax = 100;

    let data = props;

    function lookUpGrade(lookupScore: any, grades: any) {
      for (var i = 0; i < grades.length; i++) {
        if (
          grades[i].lowScore < lookupScore &&
          grades[i].highScore >= lookupScore
        ) {
          return grades[i];
        }
      }
      return null;
    }

    let chart = am4core.create(`${id}`, am4charts.GaugeChart);
    chart.hiddenState.properties.opacity = 0;
    chart.fontSize = 11;
    chart.innerRadius = am4core.percent(80);
    chart.resizable = true;

    let axis = chart.xAxes.push(new am4charts.ValueAxis<am4charts.AxisRendererCircular>());
    axis.min = chartMin;
    axis.max = chartMax;
    axis.strictMinMax = true;
    axis.renderer.radius = am4core.percent(80);
    axis.renderer.inside = true;
    axis.renderer.line.strokeOpacity = 0.1;
    axis.renderer.ticks.template.disabled = false;
    axis.renderer.ticks.template.strokeOpacity = 1;
    axis.renderer.ticks.template.strokeWidth = 0.5;
    axis.renderer.ticks.template.length = 5;
    axis.renderer.grid.template.disabled = true;
    axis.renderer.labels.template.radius = am4core.percent(15);
    axis.renderer.labels.template.fontSize = "0.9em";


    let axis2 = chart.xAxes.push(new am4charts.ValueAxis<am4charts.AxisRendererCircular>());
    axis2.min = chartMin;
    axis2.max = chartMax;
    axis2.strictMinMax = true;
    axis2.renderer.labels.template.disabled = true;
    axis2.renderer.ticks.template.disabled = true;
    axis2.renderer.grid.template.disabled = false;
    axis2.renderer.grid.template.opacity = 0.5;
    axis2.renderer.labels.template.bent = true;
    axis2.renderer.labels.template.fill = am4core.color("#000");
    axis2.renderer.labels.template.fontWeight = "bold";
    axis2.renderer.labels.template.fillOpacity = 0.3;

    for (let grading of data.gradingData) {
      let range = axis2.axisRanges.create();
      range.axisFill.fill = am4core.color(grading.color);
      range.axisFill.fillOpacity = 0.8;
      range.axisFill.zIndex = -1;
      range.value = grading.lowScore > chartMin ? grading.lowScore : chartMin;
      range.endValue = grading.highScore < chartMax ? grading.highScore : chartMax;
      range.grid.strokeOpacity = 0;
      range.label.inside = true;
      range.label.inside = true;
      range.label.location = 0.5;
      range.label.inside = true;
      range.label.paddingBottom = -5;
      range.label.fontSize = "0.9em";
    }

    let matchingGrade = lookUpGrade(data.score, data.gradingData);

    let label = chart.radarContainer.createChild(am4core.Label);
    label.isMeasured = false;
    label.fontSize = "3em";
    label.x = am4core.percent(50);
    label.paddingBottom = 15;
    label.horizontalCenter = "middle";
    label.verticalCenter = "bottom";
    label.text = data.score.toFixed(1);
    label.fill = am4core.color(matchingGrade.color);

    let hand = chart.hands.push(new am4charts.ClockHand());
    hand.axis = axis2;
    hand.innerRadius = am4core.percent(55);
    hand.startWidth = 8;
    hand.pin.disabled = true;
    hand.value = data.score;
    hand.fill = am4core.color("#444");
    hand.stroke = am4core.color("#000");
  }
}
