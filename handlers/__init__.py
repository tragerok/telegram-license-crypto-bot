"""Handlers module initialization"""

from aiogram import Dispatcher

def register_handlers(dp: Dispatcher):
    """Register all bot handlers"""
    # TODO: Import and register specific handlers
    # from .start import register_start_handlers
    # from .license import register_license_handlers
    # from .balance import register_balance_handlers
    # from .payment import register_payment_handlers
    # from .admin import register_admin_handlers
    
    # register_start_handlers(dp)
    # register_license_handlers(dp)
    # register_balance_handlers(dp)
    # register_payment_handlers(dp)
    # register_admin_handlers(dp)
    
    pass

__all__ = ['register_handlers']
