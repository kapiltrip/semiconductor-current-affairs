param(
    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Date,

    [Parameter(Mandatory = $true)]
    [string]$Headline,

    [Parameter(Mandatory = $true)]
    [string]$Summary,

    [Parameter(Mandatory = $true)]
    [string]$Url,

    [string]$Label = "SOURCE REFERENCE CARD"
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing.Common

$resolvedParent = [System.IO.Path]::GetFullPath((Split-Path -Parent $OutputPath))
if (-not [System.IO.Directory]::Exists($resolvedParent)) {
    [System.IO.Directory]::CreateDirectory($resolvedParent) | Out-Null
}

$width = 1400
$height = 800
$bitmap = [System.Drawing.Bitmap]::new($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit

$navy = [System.Drawing.ColorTranslator]::FromHtml("#002060")
$softBlue = [System.Drawing.ColorTranslator]::FromHtml("#D9E1F2")
$paleYellow = [System.Drawing.ColorTranslator]::FromHtml("#FFFF99")
$linkBlue = [System.Drawing.ColorTranslator]::FromHtml("#0563C1")
$ink = [System.Drawing.ColorTranslator]::FromHtml("#172033")
$muted = [System.Drawing.ColorTranslator]::FromHtml("#4B5563")
$white = [System.Drawing.Color]::White

$graphics.Clear($white)
$graphics.FillRectangle([System.Drawing.SolidBrush]::new($navy), 0, 0, $width, 136)
$graphics.FillRectangle([System.Drawing.SolidBrush]::new($softBlue), 0, 136, $width, 8)

$labelFont = [System.Drawing.Font]::new("Segoe UI", 18, [System.Drawing.FontStyle]::Bold)
$sourceFont = [System.Drawing.Font]::new("Segoe UI", 33, [System.Drawing.FontStyle]::Bold)
$dateFont = [System.Drawing.Font]::new("Segoe UI", 19, [System.Drawing.FontStyle]::Bold)
$headlineFont = [System.Drawing.Font]::new("Segoe UI", 38, [System.Drawing.FontStyle]::Bold)
$summaryFont = [System.Drawing.Font]::new("Segoe UI", 24, [System.Drawing.FontStyle]::Regular)
$urlFont = [System.Drawing.Font]::new("Segoe UI", 17, [System.Drawing.FontStyle]::Regular)
$noteFont = [System.Drawing.Font]::new("Segoe UI", 14, [System.Drawing.FontStyle]::Italic)

$whiteBrush = [System.Drawing.SolidBrush]::new($white)
$inkBrush = [System.Drawing.SolidBrush]::new($ink)
$mutedBrush = [System.Drawing.SolidBrush]::new($muted)
$linkBrush = [System.Drawing.SolidBrush]::new($linkBlue)
$yellowBrush = [System.Drawing.SolidBrush]::new($paleYellow)

$graphics.DrawString($Label, $labelFont, $whiteBrush, 54, 28)
$graphics.DrawString($Source, $sourceFont, $whiteBrush, 50, 62)

$dateSize = $graphics.MeasureString($Date, $dateFont)
$pillWidth = [Math]::Ceiling($dateSize.Width) + 44
$pillX = $width - $pillWidth - 54
$graphics.FillRectangle($yellowBrush, $pillX, 42, $pillWidth, 54)
$graphics.DrawString($Date, $dateFont, $inkBrush, $pillX + 22, 52)

$headlineRect = [System.Drawing.RectangleF]::new(54, 184, 1292, 250)
$graphics.DrawString($Headline, $headlineFont, $inkBrush, $headlineRect)

$graphics.FillRectangle([System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#F3F3F3")), 54, 458, 1292, 166)
$summaryRect = [System.Drawing.RectangleF]::new(78, 482, 1244, 124)
$graphics.DrawString($Summary, $summaryFont, $inkBrush, $summaryRect)

$graphics.DrawString("Verified source:", $labelFont, $mutedBrush, 54, 658)
$urlRect = [System.Drawing.RectangleF]::new(250, 657, 1096, 60)
$graphics.DrawString($Url, $urlFont, $linkBrush, $urlRect)
$graphics.DrawString("Generated from verified public headline metadata; this is a reference card, not a webpage screenshot.", $noteFont, $mutedBrush, 54, 748)

$bitmap.Save([System.IO.Path]::GetFullPath($OutputPath), [System.Drawing.Imaging.ImageFormat]::Png)

$noteFont.Dispose()
$urlFont.Dispose()
$summaryFont.Dispose()
$headlineFont.Dispose()
$dateFont.Dispose()
$sourceFont.Dispose()
$labelFont.Dispose()
$yellowBrush.Dispose()
$linkBrush.Dispose()
$mutedBrush.Dispose()
$inkBrush.Dispose()
$whiteBrush.Dispose()
$graphics.Dispose()
$bitmap.Dispose()

Write-Output ([System.IO.Path]::GetFullPath($OutputPath))
