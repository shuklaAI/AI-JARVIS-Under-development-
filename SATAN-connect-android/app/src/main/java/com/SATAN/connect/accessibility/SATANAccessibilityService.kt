package com.SATAN.connect.accessibility

import android.accessibilityservice.AccessibilityService
import android.view.accessibility.AccessibilityEvent
import com.SATAN.connect.core.AgentStateStore

class SATANAccessibilityService : AccessibilityService() {
    override fun onAccessibilityEvent(event: AccessibilityEvent?) {
        // Intentionally left blank for now.
    }

    override fun onInterrupt() {
        // Intentionally left blank for now.
    }

    override fun onServiceConnected() {
        super.onServiceConnected()
        AgentStateStore.addLog("Accessibility service enabled.")
    }
}
