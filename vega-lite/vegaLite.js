var vlSpec = {
  $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
  data: {url: '../penglings.csv'},
  width: 800,
  height: 600,
  mark: {
    type: 'point',
    filled: true,
    stroke: 'true',
    strokeWidth: 2,
    
  },
  encoding: {
    x: {
      field: 'flipper_length_mm', 
      type: 'quantitative',
      scale: {zero: false},
      axis: {title: 'Flipper Length (mm)'}
    },
    y: {
      field: 'body_mass_g', 
      type: 'quantitative',
      scale: {zero: false},
      axis: {title: 'Body Mass (g)'}
    },
    color: {
      field: 'species', 
      type: 'nominal',
      axis: {title: 'Species'},
      scale: {
        domain: ['Adelie', 'Chinstrap', 'Gentoo'],
        range: ['#FBA044', '#AA58D2', '#479F9F'],
      }
    },
    stroke: {
      field: 'species', 
      axis: {title: ''},
      type: 'nominal',
      scale: {
        domain: ['Adelie', 'Chinstrap', 'Gentoo'],
        range: ['#FBA044', '#AA58D2', '#479F9F'],
      }
    },
    size: {
      field: "bill_length_mm",
      type: "quantitative",
      axis: {title: 'Bill Length (mm)'},
      scale: {zero: false, range: [10, 500]},
    },
  },
};
// console.log(vlSpec.data)
vegaEmbed('#vis', vlSpec)