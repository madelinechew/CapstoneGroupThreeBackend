'use strict';

/**
 * test-data router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::test-data.test-data');
