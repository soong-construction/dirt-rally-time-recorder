param ($Exe = $(throw "Exe parameter is required."))

## Create new certificate (one-time)
# New-SelfSignedCertificate -Subject "CN=soong.construction.dev@gmail.com; O=github.com/soong-construction" -NotAfter (Get-Date).AddMonths(48) -Type CodeSigning -CertStoreLocation cert:\CurrentUser\My
## Export to password protected file (one-time)
# $mypwd = ConvertTo-SecureString -Force -AsPlainText
# (Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert)[0] | Export-PfxCertificate -FilePath code_signing.pfx -Password $mypwd
## or unprotected, or use certmgr.msc
# Export-Certificate -Cert (Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert)[0] -FilePath code_signing.crt
## Short circuit locally
# $env:DRTR_CODESIGN_CERTIFICATE_PASS = ConvertFrom-SecureString -SecureString $mypwd

## Apply it in CI (PWSH 6+)
try {
    $cert = Get-PfxCertificate -FilePath .\code_signing.pfx -Password (ConvertTo-SecureString -String $env:DRTR_CODESIGN_CERTIFICATE_PASS)
    Set-AuthenticodeSignature $Exe -Certificate $cert
} catch {
    Write-Host "An error occurred:"
    Write-Host $_
    Write-Host $_.ScriptStackTrace
    exit 1
}
