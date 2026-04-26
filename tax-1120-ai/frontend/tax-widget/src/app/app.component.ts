import { Component, AfterViewInit } from '@angular/core';
import Chart from 'chart.js/auto';
import { TaxService } from 'src/services/tax.services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {

  selectedFile!: File;

  result: any = null;
  preview: any[] = [];
  advice: any[] = [];
  breakdown: any = {};

  loading = false;
  totalLowConfidence = 0;

  pieChart: any;
  barChart: any;

  constructor(private taxService: TaxService) { }

  ngAfterViewInit() { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  processInsights() {
    this.totalLowConfidence = this.preview.filter(
      x => x.confidence < 0.6
    ).length;
  }

  onUpload() {




    if (!this.selectedFile) {
      alert("Select file");
      return;
    }

    this.loading = true;

    this.taxService.uploadTB(this.selectedFile).subscribe({
      next: (res: any) => {

        this.preview = res.preview || [];
        this.processInsights();

        this.result = res.result;
        this.preview = res.preview;
        this.advice = res.advice;
        this.breakdown = res.category_breakdown;

        this.loading = false;

        setTimeout(() => {
          this.renderCharts();
        }, 200); // allow DOM to load

      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    });
  }

  renderCharts() {

    // Destroy old charts (important)
    if (this.pieChart) this.pieChart.destroy();
    if (this.barChart) this.barChart.destroy();

    // PIE CHART
    const pieCtx = document.getElementById('pieChart') as any;

    this.pieChart = new Chart(pieCtx, {
      type: 'pie',
      data: {
        labels: Object.keys(this.breakdown),
        datasets: [{
          data: Object.values(this.breakdown),
        }]
      }
    });

    // BAR CHART
    const barCtx = document.getElementById('barChart') as any;

    this.barChart = new Chart(barCtx, {
      type: 'bar',
      data: {
        labels: ['Revenue', 'Deductions', 'Tax'],
        datasets: [{
          data: [
            this.result.gross_receipts,
            this.result.deductions,
            this.result.tax
          ]
        }]
      }
    });
  }
}