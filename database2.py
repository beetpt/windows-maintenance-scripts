# database.py

DATA = {
    "🌍 SCRIPTS Manutenção": sorted([
        ("🌐 (Winget) - Atualizar todos os programas instalados", "cmd /k winget upgrade --all"),
        ("🛡️ (SFC Scannow) - Verifica integridade dos ficheiros vitais", "cmd /k sfc /scannow"),
        ("🧹 Limpeza de atualizações antigas:", "cmd /k DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase"),
        ("🛠️ Comando de Reparação - (RestoreHealth)", "cmd /k DISM /Online /Cleanup-Image /RestoreHealth"),
        ("🔍 Verifica o sistema - (CheckHealth)", "cmd /k DISM /Online /Cleanup-Image /CheckHealth"),
        ("💾 Verifica integridade do Disco (sem desmontagem volume) - (CHKDSK)", "cmd /k chkdsk C: /f /r"),
        ("💾 Verifica integridade do Disco (com desmontagem volume) - (CHKDSK)", "cmd /k chkdsk C: /f /r /x"),
        ("📟 Verificar Ativação do Windows", "cmd /k slmgr.vbs /xpr"),
        ("📦 Listar Drivers Instalados", "cmd /k driverquery"),
        ("🖥️ Gerar Relatório de Energia (Bateria)", "cmd /k powercfg /energy")
    ]),

    "🌍 SCRIPTS Rede e Conetividade": sorted([
        ("🌍 Reset Total de Rede", "cmd /k ipconfig /flushdns & netsh winsock reset & netsh int ip reset"),
        ("🌍 Ver Configurações de IP", "cmd /k ipconfig /all"),
        ("🌍 Teste de Ping Contínuo (Google)", "cmd /k ping google.com -t"),
        ("🌍 Ver Portas Abertas (Netstat)", "cmd /k netstat -an | more"),
        ("🌍 Sincronizar Hora do Sistema",
         "cmd /k net stop w32time & w32tm /unregister & w32tm /register & net start w32time & w32tm /resync")
    ]),

    "🌍 SCRIPTS Diagnóstico Hardware": sorted([
        ("🌍 Gerar Relatório de Bateria (Laptop)", "cmd /k powercfg /batteryreport & start battery-report.html"),
        ("🌍 Saúde do Disco (Nova Janela)",
         "cmd /k powershell -command \"Get-PhysicalDisk | Select-Object FriendlyName, @{n='Saude(0=OK)';e={$_.HealthStatus}}, @{n='Status';e={$_.OperationalStatus}}\""),
        ("🌍 Informação Completa do Sistema", "cmd /k systeminfo"),
        ("🌍 Diagnóstico de Memória RAM", "mdsched.exe")
    ]),

    "🌍 SCRIPTS Otimização": sorted([
        ("🌍 Ativar Plano de Desempenho Máximo", "cmd /k powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"),
        ("🌍 Reparar Cache de Ícones/Explorer",
         "cmd /k taskkill /f /im explorer.exe & del /f /q %localappdata%\\IconCache.db & start explorer.exe"),
        ("🌍 Limpeza de Disco (Automática)", "cmd /k cleanmgr /d C: /lowdisk"),
        ("🌍 Reparar Windows Update", "cmd /k net stop wuauserv & net stop bits & net start wuauserv & net start bits"),
        ("🌍 Reset de Cache da Loja (WSReset)", "cmd /k wsreset.exe")
    ]),

    "🚀 Performance & Hardware": [
        ("⚡ Planos Energia", "powercfg.cpl"),
        ("📈 Monitor Recursos", "resmon"),
        ("📊 Task Manager", "taskmgr"),
        ("⚙️ Preferência Visual", "systempropertiesperformance"),
        ("📟 Gestor Dispositivos", "devmgmt.msc"),
        ("🖱️ Definições do Rato", "main.cpl"),
        ("⌨️ Definições do Teclado", "ms-settings:typing"),
        ("🎮 Definições do Joystick", "joy.cpl"),
        ("🔊 Sons Sistema", "mmsys.cpl"),
        ("📠 Impressoras", "ms-settings:printers"),
        ("🧹 Limpar fila impressão (Spooler)", 'cmd /k net stop spooler & del /Q /F /S "%systemroot%\\System32\\Spool\\Printers\\*.*" & net start spooler'),
        ("🖥️ Resolução", "desk.cpl"),
        ("📦 Armazenamento", "ms-settings:storagesense")
    ],

    "🛡️ Segurança & Kernel": [
        ("🛡️ Win Security", "ms-settings:windowsdefender"),
        ("🧱 Firewall Adv", "wf.msc"),
        ("🛡️ Definições Conta Utilizador", "useraccountcontrolsettings"),
        ("🛡️ Core Isolation", "ms-settings:coreisolation"),
        ("🔐 Certificados", "certmgr.msc"),
        ("🕵️ Prevenção DEP", "systempropertiesdataexecutionprevention"),
        ("🔐 Encriptação do Dispositivo", "ms-settings:deviceencryption"),
        ("🛡️ Contas de Utilizador", "netplwiz"),
        ("🔑 Gestor de Credenciais", "control /name Microsoft.CredentialManager")
    ],

    "🛠️ Admin & Políticas": [
        ("⚙️ Serviços", "services.msc"),
        ("📓 Registry Editor", "regedit"),
        ("📅 Agendador", "taskschd.msc"),
        ("🖥️ Gestão de Computadores", "compmgmt.msc"),
        ("📂 Variáveis de Ambiente", "rundll32.exe sysdm.cpl,EditEnvironmentVariables"),
        ("📋 Event Viewer", "eventvwr.msc"),
        ("📉 Perf Monitor", "perfmon.msc"),
        ("👥 Local Users", "lusrmgr.msc"),
        ("🛠️ Componentes do Windows", "optionalfeatures"),
        ("📦 ODBC Data", "odbcad32"),
        ("💻 COM+ Services", "comexp.msc")
    ],

    "🌐 Redes (Atalhos)": [
        ("📡 Ligações Rede", "ncpa.cpl"),
        ("🌐 Centro Rede", "control.exe /name Microsoft.NetworkAndSharingCenter"),
        ("📶 Wi-Fi Setup", "ms-settings:network-wifi"),
        ("🌍 Opções Internet", "inetcpl.cpl"),
        ("📡 Remote Desk", "systempropertiesremote"),
        ("📶 Proxy Config", "ms-settings:network-proxy"),
        ("🔗 VPN Settings", "ms-settings:network-vpn"),
        ("📡 Firewall CPL", "firewall.cpl"),
        ("🌍 Mapas Offline", "ms-settings:maps")
    ],

    "🖥️ Apps Sistema": [
        ("📝 Bloco de Notas", "notepad"),
        ("🧮 Calculadora", "calc"),
        ("🖼️ Paint", "mspaint"),
        ("📸 Ferramenta Recorte", "snippingtool"),
        ("🔍 Lupa", "magnify"),
        ("⌨️ Teclado Ecrã", "osk"),
        ("📂 Explorador Ficheiros", "explorer"),
        ("🕒 Data e Hora", "timedate.cpl")
    ],

    "🔧 Root & Reparação": [
        ("🖥️ CMD (Admin)", "cmd_admin"),
        ("📟 PowerShell (Admin)", "powershell_admin"),
        ("🔄 Restauro do Sistema", "rstrui"),
        ("🛠️ Resolução de Problemas", "control /name Microsoft.Troubleshooting"),
        ("🔄 Opções de Recuperação", "ms-settings:recovery"),
        ("💾 Gestão Discos", "diskmgmt.msc")
    ],

    "🦠 Antivírus & Segurança": [
        ("🛡️ Malwarebytes (Instalar)", "cmd /k winget install Malwarebytes.Malwarebytes --silent --accept-package-agreements"),
        ("🧹 MS Removal Tool (MRT)", "cmd /k mrt"),
        ("⚡ Scan Rápido Defender", 'cmd /k "C:\\Program Files\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 1'),
        ("🛡️ Scan Completo Defender", 'cmd /k "C:\\Program Files\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 2'),
        ("🛠️ Corrigir Win Update", "msdt.exe -id WindowsUpdateDiagnostic")
    ],

    "💽 Gestão de Discos": [
        ("🗄️ Gestão de Discos (GUI)", "diskmgmt.msc"),
        ("💻 Diskpart (Terminal)", "cmd /k diskpart"),
        ("🛠️ TestDisk & PhotoRec", "cmd /k winget install CGSecurity.TestDisk --silent --accept-package-agreements"),
        ("📊 Victoria HDD/SSD", "cmd /k winget install Victoria.Victoria --silent --accept-package-agreements"),
        ("🧹 Defraggler", "cmd /k winget install Piriform.Defraggler --silent --accept-package-agreements"),
        ("🧹 Libertar Espaço em Disco", "cleanmgr.exe"),
        ("📉 Desfragmentar Unidades", "dfrgui.exe"),
        ("🧼 Eraser (Apagar Seguro)", "cmd /k winget install Eraser.Eraser --silent --accept-package-agreements")
    ],

    "🛠️ Download utilitários": sorted([
        ("Instalar AnyDesk", "cmd /k winget install AnyDesk.AnyDesk --silent --accept-package-agreements"),
        ("Instalar 7-Zip", "cmd /k winget install 7zip.7zip --silent"),
        ("Instalar WinRAR", "cmd /k winget install RARLab.WinRAR --silent"),
        ("Instalar Notepad++", "cmd /k winget install Notepad++"),
        ("REPARAR WINGET (Caso falhe)", "cmd /k winget source reset --force"),
        ("Instalar VLC Media Player", "cmd /k winget install VideoLAN.VLC --silent --accept-package-agreements"),
        ("Instalar Foxit PDF Reader", "cmd /k winget install Foxit.FoxitReader --silent --accept-package-agreements"),
        ("Instalar CPU-Z (Hardware)", "cmd /k winget install CPUID.CPU-Z --silent --accept-package-agreements"),
        ("Instalar CrystalDiskInfo", "cmd /k winget install CrystalDewWorld.CrystalDiskInfo --silent --accept-package-agreements"),
        ("Instalar Java Runtime", "cmd /k winget install Oracle.JavaRuntimeEnvironment --silent --accept-package-agreements"),
        ("Instalar Revo Uninstaller", "cmd /k winget install RevoUninstaller.RevoUninstaller --silent --accept-package-agreements"),
        ("Instalar qBittorrent", "cmd /k winget install qBittorrent.qBittorrent --silent --accept-package-agreements")
    ]),

    "📂 Abrir Discos": sorted([
        ("Abrir Disco C:", "C:"),
        ("Abrir Disco D:", "D:"),
        ("Abrir Disco E:", "E:"),
        ("Abrir Disco F:", "F:"),
        ("Abrir Disco G:", "G:")
    ]),


    "⭐ MODO GOD": [
        ("🆘 ABRIR PASTA GOD MODE", "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}")
    ]
}