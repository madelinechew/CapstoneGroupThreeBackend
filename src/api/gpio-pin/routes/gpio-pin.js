'use strict';

/**
 * gpio-pin router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::gpio-pin.gpio-pin');
