{{ with $todayWeather := index .Weathers 0 }}

`{{ $todayWeather.City }}, {{$todayWeather.Country }} - {{ formatDate $todayWeather.StartTime $todayWeather.Timezone }}`

<img src="{{ $todayWeather.Icon}}"/>

{{ $todayWeather.Condition }}

{{template "hourly-table" $todayWeather.HourlyWeathers}}

{{- end }}

<div align="right">

*Updated at: {{formatTime .UpdatedAt}} - by **[mindongun123/weather-forecast](https://github.com/mindongun123/weather-forecast)***

</div>
