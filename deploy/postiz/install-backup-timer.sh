#!/usr/bin/env bash
set -euo pipefail
release=${1:?Absolute release directory}
operator=${2:?Protected operator.env path}
[[ "$release" =~ ^/[a-zA-Z0-9/_-]+$ && "$operator" =~ ^/[a-zA-Z0-9/_.-]+$ ]]
[[ $(loginctl show-user "$USER" -p Linger --value) == yes ]]
units="$HOME/.config/systemd/user"
mkdir -p "$units"
cat > "$units/wlkrlabs-postiz-backup.service" <<EOF
[Unit]
Description=Consistent WLKR Labs Postiz backup
[Service]
Type=oneshot
TimeoutStartSec=900
Environment=POSTIZ_OPERATOR_ENV=$operator
ExecStart=$release/backup.sh
EOF
cat > "$units/wlkrlabs-postiz-backup.timer" <<'EOF'
[Unit]
Description=Back up Postiz before the existing host snapshot
[Timer]
OnCalendar=*-*-* 01:30:00
Persistent=true
RandomizedDelaySec=120
[Install]
WantedBy=timers.target
EOF
systemctl --user daemon-reload
systemctl --user enable --now wlkrlabs-postiz-backup.timer
