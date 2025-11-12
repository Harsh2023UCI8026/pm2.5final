fetch("/forecast")
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('pm25Chart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.timestamps,
        datasets: [{
          label: 'Predicted PM2.5',
          data: data.values,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  });
