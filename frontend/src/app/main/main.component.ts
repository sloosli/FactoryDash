import {Component, OnInit} from "@angular/core";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";

@Component({
  selector: 'main',
  templateUrl: 'main.component.html',
  styleUrls: ['main.component.scss']
}) export class MainComponent implements OnInit{

  public koefArr: number[] = [67, 22, 100, 88];
  public chartIds: string[] = [];

  public ngOnInit(): void {
    let chartCounter = 1;
    for (let koef of this.koefArr) {
      this.createSpeedCheck(koef, chartCounter++);
    }
  }

  private createSpeedCheck(koef: number, chartCounter: number): void {
    let id = `chart${chartCounter}`
    this.chartIds.push(id);
    let chart = am4core.create(`${id}`, am4charts.GaugeChart);
    let axis = chart.xAxes.push(new am4charts.ValueAxis<am4charts.AxisRendererCircular>());
    axis.min = 0;
    axis.max = 100;
    axis.strictMinMax = true;
    chart.innerRadius = -20;
    chart.startAngle = -180;
    chart.endAngle = 0;

    let range = axis.axisRanges.create();
    range.value = 0;
    range.endValue = 100;
    range.axisFill.fillOpacity = 1;
    range.axisFill.fill = am4core.color("#88AB75");
    range.axisFill.zIndex = 1;

    let hand = chart.hands.push(new am4charts.ClockHand());
    hand.value = koef;
    hand.pin.disabled = true;
  }
}

